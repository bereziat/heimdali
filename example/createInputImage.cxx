#include "heimdali/itkhelper.hxx"
#include <itkImageRegionIterator.h>

int main()
{
    // Create image.
    unsigned int nx = 5;
    unsigned int ny = 5;
    unsigned int nz = 5;
    unsigned int nv = 2;
    Heimdali::ImageFloat::Pointer image = Heimdali::CreateImage(nx,ny,nz,nv);

    // Pixel vector.
    typedef itk::VariableLengthVector<double> VariableVectorType;
    VariableVectorType value;
    value.SetSize(nv);

    // Set image values.
    typedef itk::ImageRegionIterator<Heimdali::ImageFloat> IteratorType;
    IteratorType imageIt(image, image->GetLargestPossibleRegion());
    Heimdali::ImageFloat::IndexType index;
    for(imageIt.GoToBegin(); !imageIt.IsAtEnd(); ++imageIt) {
      index = imageIt.GetIndex();
      unsigned int ix = index[0];
      unsigned int iy = index[1];
      float x = float (ix) / float(nx); // x is in [0,1]
      float y = float (iy) / float(ny); // x is in [0,1]
      value[0] = cos(x)*cos(y);
      value[1] = sin(x)*sin(y);
      imageIt.Set(value);
    }

    // Save image.
    Heimdali::OpenAndWriteImage("image.h5", image);
}
